# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .apikey import *
from .get_namespaces import *
from .get_regions import *
from .namespace import *
from .namespace_search_attribute import *
from .provider import *
from .service_account import *
from .user import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_temporalcloud.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_temporalcloud.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "temporalcloud",
  "mod": "index/apikey",
  "fqn": "pulumi_temporalcloud",
  "classes": {
   "temporalcloud:index/apikey:Apikey": "Apikey"
  }
 },
 {
  "pkg": "temporalcloud",
  "mod": "index/namespace",
  "fqn": "pulumi_temporalcloud",
  "classes": {
   "temporalcloud:index/namespace:Namespace": "Namespace"
  }
 },
 {
  "pkg": "temporalcloud",
  "mod": "index/namespaceSearchAttribute",
  "fqn": "pulumi_temporalcloud",
  "classes": {
   "temporalcloud:index/namespaceSearchAttribute:NamespaceSearchAttribute": "NamespaceSearchAttribute"
  }
 },
 {
  "pkg": "temporalcloud",
  "mod": "index/serviceAccount",
  "fqn": "pulumi_temporalcloud",
  "classes": {
   "temporalcloud:index/serviceAccount:ServiceAccount": "ServiceAccount"
  }
 },
 {
  "pkg": "temporalcloud",
  "mod": "index/user",
  "fqn": "pulumi_temporalcloud",
  "classes": {
   "temporalcloud:index/user:User": "User"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "temporalcloud",
  "token": "pulumi:providers:temporalcloud",
  "fqn": "pulumi_temporalcloud",
  "class": "Provider"
 }
]
"""
)
