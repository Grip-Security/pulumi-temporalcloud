// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace GripSecurity.PulumiTemporalCloud
{
    /// <summary>
    /// Provisions a Temporal Cloud user.
    /// 
    /// ## Import
    /// 
    /// Users can be imported to incorporate existing Users into your Terraform pipeline.
    /// 
    /// To import a User, you need
    /// 
    /// - a resource configuration in your Terraform configuration file/module to accept the imported User. In the example below, the placeholder is "temporalcloud_user" "user"
    /// 
    /// - the User's ID, which is found using the Temporal Cloud CLI tcld u l. In the example below, this is 72360058153949edb2f1d47019c1e85f
    /// 
    /// ```sh
    /// $ pulumi import temporalcloud:index/user:User user 72360058153949edb2f1d47019c1e85f
    /// ```
    /// </summary>
    [PulumiTemporalCloudResourceType("temporalcloud:index/user:User")]
    public partial class User : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The role on the account. Must be one of owner, admin, developer, or read (case-insensitive). owner is only valid for import and cannot be created, updated or deleted without Temporal support.
        /// </summary>
        [Output("accountAccess")]
        public Output<string> AccountAccess { get; private set; } = null!;

        /// <summary>
        /// The email address for the user.
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Users with account*access roles of owner or admin cannot be assigned explicit permissions to namespaces. They implicitly receive access to all Namespaces.
        /// </summary>
        [Output("namespaceAccesses")]
        public Output<ImmutableArray<Outputs.UserNamespaceAccess>> NamespaceAccesses { get; private set; } = null!;

        /// <summary>
        /// The current state of the user.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        [Output("timeouts")]
        public Output<Outputs.UserTimeouts?> Timeouts { get; private set; } = null!;


        /// <summary>
        /// Create a User resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public User(string name, UserArgs args, CustomResourceOptions? options = null)
            : base("temporalcloud:index/user:User", name, args ?? new UserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private User(string name, Input<string> id, UserState? state = null, CustomResourceOptions? options = null)
            : base("temporalcloud:index/user:User", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing User resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static User Get(string name, Input<string> id, UserState? state = null, CustomResourceOptions? options = null)
        {
            return new User(name, id, state, options);
        }
    }

    public sealed class UserArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The role on the account. Must be one of owner, admin, developer, or read (case-insensitive). owner is only valid for import and cannot be created, updated or deleted without Temporal support.
        /// </summary>
        [Input("accountAccess", required: true)]
        public Input<string> AccountAccess { get; set; } = null!;

        /// <summary>
        /// The email address for the user.
        /// </summary>
        [Input("email", required: true)]
        public Input<string> Email { get; set; } = null!;

        [Input("namespaceAccesses")]
        private InputList<Inputs.UserNamespaceAccessArgs>? _namespaceAccesses;

        /// <summary>
        /// The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Users with account*access roles of owner or admin cannot be assigned explicit permissions to namespaces. They implicitly receive access to all Namespaces.
        /// </summary>
        public InputList<Inputs.UserNamespaceAccessArgs> NamespaceAccesses
        {
            get => _namespaceAccesses ?? (_namespaceAccesses = new InputList<Inputs.UserNamespaceAccessArgs>());
            set => _namespaceAccesses = value;
        }

        [Input("timeouts")]
        public Input<Inputs.UserTimeoutsArgs>? Timeouts { get; set; }

        public UserArgs()
        {
        }
        public static new UserArgs Empty => new UserArgs();
    }

    public sealed class UserState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The role on the account. Must be one of owner, admin, developer, or read (case-insensitive). owner is only valid for import and cannot be created, updated or deleted without Temporal support.
        /// </summary>
        [Input("accountAccess")]
        public Input<string>? AccountAccess { get; set; }

        /// <summary>
        /// The email address for the user.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        [Input("namespaceAccesses")]
        private InputList<Inputs.UserNamespaceAccessGetArgs>? _namespaceAccesses;

        /// <summary>
        /// The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Users with account*access roles of owner or admin cannot be assigned explicit permissions to namespaces. They implicitly receive access to all Namespaces.
        /// </summary>
        public InputList<Inputs.UserNamespaceAccessGetArgs> NamespaceAccesses
        {
            get => _namespaceAccesses ?? (_namespaceAccesses = new InputList<Inputs.UserNamespaceAccessGetArgs>());
            set => _namespaceAccesses = value;
        }

        /// <summary>
        /// The current state of the user.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        [Input("timeouts")]
        public Input<Inputs.UserTimeoutsGetArgs>? Timeouts { get; set; }

        public UserState()
        {
        }
        public static new UserState Empty => new UserState();
    }
}
