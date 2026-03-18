from namecheap_wrapper.schemas.config import NamecheapConfig
from namecheap_wrapper.client.client import NamecheapClient
from namecheap_wrapper.services.ssl import SSLService


class Namecheap:

    def __init__(self, config: NamecheapConfig):
        self.config = config
        self.client = NamecheapClient(config)
        self.ssl = SSLService(self.client)
