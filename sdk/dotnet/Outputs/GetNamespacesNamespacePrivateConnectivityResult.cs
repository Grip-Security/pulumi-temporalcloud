// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace GripSecurity.PulumiTemporalCloud.Outputs
{

    [OutputType]
    public sealed class GetNamespacesNamespacePrivateConnectivityResult
    {
        /// <summary>
        /// The AWS PrivateLink info. This will only be set for namespaces whose cloud provider is AWS.
        /// </summary>
        public readonly Outputs.GetNamespacesNamespacePrivateConnectivityAwsPrivateLinkInfoResult AwsPrivateLinkInfo;
        /// <summary>
        /// The id of the region where the private connectivity applies.
        /// </summary>
        public readonly string Region;

        [OutputConstructor]
        private GetNamespacesNamespacePrivateConnectivityResult(
            Outputs.GetNamespacesNamespacePrivateConnectivityAwsPrivateLinkInfoResult awsPrivateLinkInfo,

            string region)
        {
            AwsPrivateLinkInfo = awsPrivateLinkInfo;
            Region = region;
        }
    }
}
