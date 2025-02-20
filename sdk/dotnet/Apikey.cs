// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace GripSecurity.Temporalcloud
{
    /// <summary>
    /// Provisions a Temporal Cloud API key.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Temporalcloud = GripSecurity.Temporalcloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var globalServiceAccount = new Temporalcloud.ServiceAccount("global_service_account", new()
    ///     {
    ///         Name = "admin",
    ///         AccountAccess = "Admin",
    ///     });
    /// 
    ///     var globalApikey = new Temporalcloud.Apikey("global_apikey", new()
    ///     {
    ///         DisplayName = "admin",
    ///         OwnerType = "service-account",
    ///         OwnerId = globalServiceAccount.Id,
    ///         ExpiryTime = "2024-11-01T00:00:00Z",
    ///         Disabled = false,
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [TemporalcloudResourceType("temporalcloud:index/apikey:Apikey")]
    public partial class Apikey : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The description for the API key.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Whether the API key is disabled.
        /// </summary>
        [Output("disabled")]
        public Output<bool> Disabled { get; private set; } = null!;

        /// <summary>
        /// The display name for the API key.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// The expiry time for the API key in ISO 8601 format.
        /// </summary>
        [Output("expiryTime")]
        public Output<string> ExpiryTime { get; private set; } = null!;

        /// <summary>
        /// The ID of the owner to create the API key for.
        /// </summary>
        [Output("ownerId")]
        public Output<string> OwnerId { get; private set; } = null!;

        /// <summary>
        /// The type of the owner to create the API key.
        /// </summary>
        [Output("ownerType")]
        public Output<string> OwnerType { get; private set; } = null!;

        /// <summary>
        /// The current state of the API key.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        [Output("timeouts")]
        public Output<Outputs.ApikeyTimeouts?> Timeouts { get; private set; } = null!;

        [Output("token")]
        public Output<string> Token { get; private set; } = null!;


        /// <summary>
        /// Create a Apikey resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Apikey(string name, ApikeyArgs args, CustomResourceOptions? options = null)
            : base("temporalcloud:index/apikey:Apikey", name, args ?? new ApikeyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Apikey(string name, Input<string> id, ApikeyState? state = null, CustomResourceOptions? options = null)
            : base("temporalcloud:index/apikey:Apikey", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/Grip-Security/pulumi-temporalcloud/releases/download/v${VERSION}/",
                AdditionalSecretOutputs =
                {
                    "token",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Apikey resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Apikey Get(string name, Input<string> id, ApikeyState? state = null, CustomResourceOptions? options = null)
        {
            return new Apikey(name, id, state, options);
        }
    }

    public sealed class ApikeyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description for the API key.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Whether the API key is disabled.
        /// </summary>
        [Input("disabled")]
        public Input<bool>? Disabled { get; set; }

        /// <summary>
        /// The display name for the API key.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// The expiry time for the API key in ISO 8601 format.
        /// </summary>
        [Input("expiryTime", required: true)]
        public Input<string> ExpiryTime { get; set; } = null!;

        /// <summary>
        /// The ID of the owner to create the API key for.
        /// </summary>
        [Input("ownerId", required: true)]
        public Input<string> OwnerId { get; set; } = null!;

        /// <summary>
        /// The type of the owner to create the API key.
        /// </summary>
        [Input("ownerType", required: true)]
        public Input<string> OwnerType { get; set; } = null!;

        [Input("timeouts")]
        public Input<Inputs.ApikeyTimeoutsArgs>? Timeouts { get; set; }

        public ApikeyArgs()
        {
        }
        public static new ApikeyArgs Empty => new ApikeyArgs();
    }

    public sealed class ApikeyState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description for the API key.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Whether the API key is disabled.
        /// </summary>
        [Input("disabled")]
        public Input<bool>? Disabled { get; set; }

        /// <summary>
        /// The display name for the API key.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// The expiry time for the API key in ISO 8601 format.
        /// </summary>
        [Input("expiryTime")]
        public Input<string>? ExpiryTime { get; set; }

        /// <summary>
        /// The ID of the owner to create the API key for.
        /// </summary>
        [Input("ownerId")]
        public Input<string>? OwnerId { get; set; }

        /// <summary>
        /// The type of the owner to create the API key.
        /// </summary>
        [Input("ownerType")]
        public Input<string>? OwnerType { get; set; }

        /// <summary>
        /// The current state of the API key.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        [Input("timeouts")]
        public Input<Inputs.ApikeyTimeoutsGetArgs>? Timeouts { get; set; }

        [Input("token")]
        private Input<string>? _token;
        public Input<string>? Token
        {
            get => _token;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _token = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public ApikeyState()
        {
        }
        public static new ApikeyState Empty => new ApikeyState();
    }
}
