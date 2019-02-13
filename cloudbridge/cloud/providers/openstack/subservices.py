import logging

from cloudbridge.cloud.base.subservices import BaseBucketObjectSubService
from cloudbridge.cloud.base.subservices import BaseFloatingIPSubService
from cloudbridge.cloud.base.subservices import BaseGatewaySubService
from cloudbridge.cloud.base.subservices import \
    BaseVMFirewallRuleSubService


log = logging.getLogger(__name__)


class OpenStackBucketObjectSubService(BaseBucketObjectSubService):

    def __init__(self, provider, bucket):
        super(OpenStackBucketObjectSubService, self).__init__(provider, bucket)


class OpenStackGatewaySubService(BaseGatewaySubService):

    def __init__(self, provider, network):
        super(OpenStackGatewaySubService, self).__init__(provider, network)


class OpenStackFloatingIPSubService(BaseFloatingIPSubService):

    def __init__(self, provider, gateway):
        super(OpenStackFloatingIPSubService, self).__init__(provider, gateway)


class OpenStackVMFirewallRuleSubService(BaseVMFirewallRuleSubService):

    def __init__(self, provider, firewall):
        super(OpenStackVMFirewallRuleSubService, self).__init__(
            provider, firewall)
