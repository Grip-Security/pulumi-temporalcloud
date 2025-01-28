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
    public sealed class NamespaceEndpoints
    {
        /// <summary>
        /// The gRPC address for API key client connections (may be empty if API keys are disabled).
        /// </summary>
        public readonly string? GrpcAddress;
        /// <summary>
        /// The gRPC address for mTLS client connections (may be empty if mTLS is disabled).
        /// </summary>
        public readonly string? MtlsGrpcAddress;
        /// <summary>
        /// The address in the Temporal Cloud Web UI for the namespace
        /// </summary>
        public readonly string? WebAddress;

        [OutputConstructor]
        private NamespaceEndpoints(
            string? grpcAddress,

            string? mtlsGrpcAddress,

            string? webAddress)
        {
            GrpcAddress = grpcAddress;
            MtlsGrpcAddress = mtlsGrpcAddress;
            WebAddress = webAddress;
        }
    }
}
