import sys
import os
import grpc

# Path to the lnd directory that contains lnrpc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lnd')))

import lnrpc.lightning_pb2 as ln # pyright: ignore[reportMissingImports]
import lnrpc.lightning_pb2_grpc as lnrpc # pyright: ignore[reportMissingImports]

class LightningClient:
    def __init__(self, lnd_host='localhost:10009', tls_cert_path='tls.cert', macaroon_path='admin.macaroon'):
        # Read TLS certificate
        with open(tls_cert_path, 'rb') as f:
            cert = f.read()
        creds = grpc.ssl_channel_credentials(cert)

        # Read macaroon and convert to hex string
        with open(macaroon_path, 'rb') as f:
            macaroon_bytes = f.read()
        macaroon = macaroon_bytes.hex()

        # Create metadata credentials with macaroon
        def metadata_callback(context, callback):
            callback([('macaroon', macaroon)], None)

        auth_creds = grpc.metadata_call_credentials(metadata_callback)
        combined_creds = grpc.composite_channel_credentials(creds, auth_creds)
        
        # Create secure gRPC channel
        self.channel = grpc.secure_channel(lnd_host, combined_creds)
        self.stub = lnrpc.LightningStub(self.channel)

    def create_invoice(self, amount_sats: int, memo: str = "Invoice from FastAPI"):
        invoice = ln.Invoice(value=amount_sats, memo=memo)
        response = self.stub.AddInvoice(invoice)
        return {
            "payment_request": response.payment_request,
            "r_hash": response.r_hash.hex()
        }