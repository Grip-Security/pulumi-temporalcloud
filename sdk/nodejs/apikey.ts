// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provisions a Temporal Cloud API key.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as temporalcloud from "@grip-security/pulumi-temporalcloud";
 *
 * const globalServiceAccount = new temporalcloud.ServiceAccount("global_service_account", {
 *     name: "admin",
 *     accountAccess: "Admin",
 * });
 * const globalApikey = new temporalcloud.Apikey("global_apikey", {
 *     displayName: "admin",
 *     ownerType: "service-account",
 *     ownerId: globalServiceAccount.id,
 *     expiryTime: "2024-11-01T00:00:00Z",
 *     disabled: false,
 * });
 * ```
 */
export class Apikey extends pulumi.CustomResource {
    /**
     * Get an existing Apikey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApikeyState, opts?: pulumi.CustomResourceOptions): Apikey {
        return new Apikey(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'temporalcloud:index/apikey:Apikey';

    /**
     * Returns true if the given object is an instance of Apikey.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Apikey {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Apikey.__pulumiType;
    }

    /**
     * The description for the API key.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Whether the API key is disabled.
     */
    public readonly disabled!: pulumi.Output<boolean>;
    /**
     * The display name for the API key.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * The expiry time for the API key in ISO 8601 format.
     */
    public readonly expiryTime!: pulumi.Output<string>;
    /**
     * The ID of the owner to create the API key for.
     */
    public readonly ownerId!: pulumi.Output<string>;
    /**
     * The type of the owner to create the API key.
     */
    public readonly ownerType!: pulumi.Output<string>;
    /**
     * The current state of the API key.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    public readonly timeouts!: pulumi.Output<outputs.ApikeyTimeouts | undefined>;
    public /*out*/ readonly token!: pulumi.Output<string>;

    /**
     * Create a Apikey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApikeyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApikeyArgs | ApikeyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ApikeyState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["disabled"] = state ? state.disabled : undefined;
            resourceInputs["displayName"] = state ? state.displayName : undefined;
            resourceInputs["expiryTime"] = state ? state.expiryTime : undefined;
            resourceInputs["ownerId"] = state ? state.ownerId : undefined;
            resourceInputs["ownerType"] = state ? state.ownerType : undefined;
            resourceInputs["state"] = state ? state.state : undefined;
            resourceInputs["timeouts"] = state ? state.timeouts : undefined;
            resourceInputs["token"] = state ? state.token : undefined;
        } else {
            const args = argsOrState as ApikeyArgs | undefined;
            if ((!args || args.displayName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'displayName'");
            }
            if ((!args || args.expiryTime === undefined) && !opts.urn) {
                throw new Error("Missing required property 'expiryTime'");
            }
            if ((!args || args.ownerId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ownerId'");
            }
            if ((!args || args.ownerType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ownerType'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["disabled"] = args ? args.disabled : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["expiryTime"] = args ? args.expiryTime : undefined;
            resourceInputs["ownerId"] = args ? args.ownerId : undefined;
            resourceInputs["ownerType"] = args ? args.ownerType : undefined;
            resourceInputs["timeouts"] = args ? args.timeouts : undefined;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["token"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["token"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Apikey.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Apikey resources.
 */
export interface ApikeyState {
    /**
     * The description for the API key.
     */
    description?: pulumi.Input<string>;
    /**
     * Whether the API key is disabled.
     */
    disabled?: pulumi.Input<boolean>;
    /**
     * The display name for the API key.
     */
    displayName?: pulumi.Input<string>;
    /**
     * The expiry time for the API key in ISO 8601 format.
     */
    expiryTime?: pulumi.Input<string>;
    /**
     * The ID of the owner to create the API key for.
     */
    ownerId?: pulumi.Input<string>;
    /**
     * The type of the owner to create the API key.
     */
    ownerType?: pulumi.Input<string>;
    /**
     * The current state of the API key.
     */
    state?: pulumi.Input<string>;
    timeouts?: pulumi.Input<inputs.ApikeyTimeouts>;
    token?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Apikey resource.
 */
export interface ApikeyArgs {
    /**
     * The description for the API key.
     */
    description?: pulumi.Input<string>;
    /**
     * Whether the API key is disabled.
     */
    disabled?: pulumi.Input<boolean>;
    /**
     * The display name for the API key.
     */
    displayName: pulumi.Input<string>;
    /**
     * The expiry time for the API key in ISO 8601 format.
     */
    expiryTime: pulumi.Input<string>;
    /**
     * The ID of the owner to create the API key for.
     */
    ownerId: pulumi.Input<string>;
    /**
     * The type of the owner to create the API key.
     */
    ownerType: pulumi.Input<string>;
    timeouts?: pulumi.Input<inputs.ApikeyTimeouts>;
}
