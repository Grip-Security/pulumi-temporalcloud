// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as enums from "./types/enums";
import * as utilities from "./utilities";

/**
 * Provisions a Temporal Cloud user.
 *
 * ## Import
 *
 * Users can be imported to incorporate existing Users into your Terraform pipeline.
 *
 * To import a User, you need
 *
 * - a resource configuration in your Terraform configuration file/module to accept the imported User. In the example below, the placeholder is "temporalcloud_user" "user"
 *
 * - the User's ID, which is found using the Temporal Cloud CLI tcld u l. In the example below, this is 72360058153949edb2f1d47019c1e85f
 *
 * ```sh
 * $ pulumi import temporalcloud:index/user:User user 72360058153949edb2f1d47019c1e85f
 * ```
 */
export class User extends pulumi.CustomResource {
    /**
     * Get an existing User resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState, opts?: pulumi.CustomResourceOptions): User {
        return new User(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'temporalcloud:index/user:User';

    /**
     * Returns true if the given object is an instance of User.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is User {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === User.__pulumiType;
    }

    /**
     * The role on the account. Must be one of owner, admin, developer, or read (case-insensitive). owner is only valid for import and cannot be created, updated or deleted without Temporal support.
     */
    public readonly accountAccess!: pulumi.Output<string>;
    /**
     * The email address for the user.
     */
    public readonly email!: pulumi.Output<string>;
    /**
     * The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Users with account*access roles of owner or admin cannot be assigned explicit permissions to namespaces. They implicitly receive access to all Namespaces.
     */
    public readonly namespaceAccesses!: pulumi.Output<outputs.UserNamespaceAccess[] | undefined>;
    /**
     * The current state of the user.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    public readonly timeouts!: pulumi.Output<outputs.UserTimeouts | undefined>;

    /**
     * Create a User resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserArgs | UserState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as UserState | undefined;
            resourceInputs["accountAccess"] = state ? state.accountAccess : undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["namespaceAccesses"] = state ? state.namespaceAccesses : undefined;
            resourceInputs["state"] = state ? state.state : undefined;
            resourceInputs["timeouts"] = state ? state.timeouts : undefined;
        } else {
            const args = argsOrState as UserArgs | undefined;
            if ((!args || args.accountAccess === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accountAccess'");
            }
            if ((!args || args.email === undefined) && !opts.urn) {
                throw new Error("Missing required property 'email'");
            }
            resourceInputs["accountAccess"] = args ? args.accountAccess : undefined;
            resourceInputs["email"] = args ? args.email : undefined;
            resourceInputs["namespaceAccesses"] = args ? args.namespaceAccesses : undefined;
            resourceInputs["timeouts"] = args ? args.timeouts : undefined;
            resourceInputs["state"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(User.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering User resources.
 */
export interface UserState {
    /**
     * The role on the account. Must be one of owner, admin, developer, or read (case-insensitive). owner is only valid for import and cannot be created, updated or deleted without Temporal support.
     */
    accountAccess?: pulumi.Input<string>;
    /**
     * The email address for the user.
     */
    email?: pulumi.Input<string>;
    /**
     * The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Users with account*access roles of owner or admin cannot be assigned explicit permissions to namespaces. They implicitly receive access to all Namespaces.
     */
    namespaceAccesses?: pulumi.Input<pulumi.Input<inputs.UserNamespaceAccess>[]>;
    /**
     * The current state of the user.
     */
    state?: pulumi.Input<string>;
    timeouts?: pulumi.Input<inputs.UserTimeouts>;
}

/**
 * The set of arguments for constructing a User resource.
 */
export interface UserArgs {
    /**
     * The role on the account. Must be one of owner, admin, developer, or read (case-insensitive). owner is only valid for import and cannot be created, updated or deleted without Temporal support.
     */
    accountAccess: pulumi.Input<string>;
    /**
     * The email address for the user.
     */
    email: pulumi.Input<string>;
    /**
     * The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Users with account*access roles of owner or admin cannot be assigned explicit permissions to namespaces. They implicitly receive access to all Namespaces.
     */
    namespaceAccesses?: pulumi.Input<pulumi.Input<inputs.UserNamespaceAccess>[]>;
    timeouts?: pulumi.Input<inputs.UserTimeouts>;
}
