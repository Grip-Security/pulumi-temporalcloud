// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace GripSecurity.Temporalcloud.Inputs
{

    public sealed class NamespaceCertificateFilterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The certificate's common name.
        /// </summary>
        [Input("commonName")]
        public Input<string>? CommonName { get; set; }

        /// <summary>
        /// The certificate's organization.
        /// </summary>
        [Input("organization")]
        public Input<string>? Organization { get; set; }

        /// <summary>
        /// The certificate's organizational unit.
        /// </summary>
        [Input("organizationalUnit")]
        public Input<string>? OrganizationalUnit { get; set; }

        /// <summary>
        /// The certificate's subject alternative name (or SAN).
        /// </summary>
        [Input("subjectAlternativeName")]
        public Input<string>? SubjectAlternativeName { get; set; }

        public NamespaceCertificateFilterArgs()
        {
        }
        public static new NamespaceCertificateFilterArgs Empty => new NamespaceCertificateFilterArgs();
    }
}
