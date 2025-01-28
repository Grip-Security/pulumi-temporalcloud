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
    public sealed class GetNamespacesNamespaceCodecServerResult
    {
        /// <summary>
        /// The endpoint of the codec server.
        /// </summary>
        public readonly string Endpoint;
        /// <summary>
        /// If true, Temporal Cloud will include cross-origin credentials in requests to the codec server.
        /// </summary>
        public readonly bool IncludeCrossOriginCredentials;
        /// <summary>
        /// If true, Temporal Cloud will pass the access token to the codec server upon each request.
        /// </summary>
        public readonly bool PassAccessToken;

        [OutputConstructor]
        private GetNamespacesNamespaceCodecServerResult(
            string endpoint,

            bool includeCrossOriginCredentials,

            bool passAccessToken)
        {
            Endpoint = endpoint;
            IncludeCrossOriginCredentials = includeCrossOriginCredentials;
            PassAccessToken = passAccessToken;
        }
    }
}