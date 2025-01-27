// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provisions a Temporal Cloud Nexus endpoint.
 *
 * ## Import
 *
 * Nexus Endpoints can be imported to incorporate existing Nexus Endpoints into your Terraform pipeline.
 *
 * To import a Nexus Endpoint, you need
 *
 * - a resource configuration in your Terraform configuration file/module to accept the imported Nexus Endpoint. In the example below, the placeholder is "temporalcloud_nexus_endpoint" "nexus_endpoint"
 *
 * - the Nexus Endpoint's ID, which is found using the Temporal Cloud CLI tcld nexus endpoint list. In the example below, this is 405f7da4224a43d99c211904ed9b3819
 *
 * ```sh
 * $ pulumi import temporalcloud:index/nexusEndpoint:NexusEndpoint nexus_endpoint 405f7da4224a43d99c211904ed9b3819
 * ```
 */
export class NexusEndpoint extends pulumi.CustomResource {
    /**
     * Get an existing NexusEndpoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NexusEndpointState, opts?: pulumi.CustomResourceOptions): NexusEndpoint {
        return new NexusEndpoint(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'temporalcloud:index/nexusEndpoint:NexusEndpoint';

    /**
     * Returns true if the given object is an instance of NexusEndpoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NexusEndpoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NexusEndpoint.__pulumiType;
    }

    /**
     * Namespace Id(s) that are allowed to call this Endpoint.
     */
    public readonly allowedCallerNamespaces!: pulumi.Output<string[]>;
    /**
     * The description for the Nexus endpoint.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the endpoint. Must be unique within an account and match `^[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9]$`
     */
    public readonly name!: pulumi.Output<string>;
    public readonly timeouts!: pulumi.Output<outputs.NexusEndpointTimeouts | undefined>;
    /**
     * A target spec for routing nexus requests to a specific cloud namespace worker.
     */
    public readonly workerTarget!: pulumi.Output<outputs.NexusEndpointWorkerTarget>;

    /**
     * Create a NexusEndpoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NexusEndpointArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NexusEndpointArgs | NexusEndpointState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NexusEndpointState | undefined;
            resourceInputs["allowedCallerNamespaces"] = state ? state.allowedCallerNamespaces : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["timeouts"] = state ? state.timeouts : undefined;
            resourceInputs["workerTarget"] = state ? state.workerTarget : undefined;
        } else {
            const args = argsOrState as NexusEndpointArgs | undefined;
            if ((!args || args.allowedCallerNamespaces === undefined) && !opts.urn) {
                throw new Error("Missing required property 'allowedCallerNamespaces'");
            }
            if ((!args || args.workerTarget === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workerTarget'");
            }
            resourceInputs["allowedCallerNamespaces"] = args ? args.allowedCallerNamespaces : undefined;
            resourceInputs["description"] = args?.description ? pulumi.secret(args.description) : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["timeouts"] = args ? args.timeouts : undefined;
            resourceInputs["workerTarget"] = args ? args.workerTarget : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["description"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(NexusEndpoint.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NexusEndpoint resources.
 */
export interface NexusEndpointState {
    /**
     * Namespace Id(s) that are allowed to call this Endpoint.
     */
    allowedCallerNamespaces?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The description for the Nexus endpoint.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the endpoint. Must be unique within an account and match `^[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9]$`
     */
    name?: pulumi.Input<string>;
    timeouts?: pulumi.Input<inputs.NexusEndpointTimeouts>;
    /**
     * A target spec for routing nexus requests to a specific cloud namespace worker.
     */
    workerTarget?: pulumi.Input<inputs.NexusEndpointWorkerTarget>;
}

/**
 * The set of arguments for constructing a NexusEndpoint resource.
 */
export interface NexusEndpointArgs {
    /**
     * Namespace Id(s) that are allowed to call this Endpoint.
     */
    allowedCallerNamespaces: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The description for the Nexus endpoint.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the endpoint. Must be unique within an account and match `^[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9]$`
     */
    name?: pulumi.Input<string>;
    timeouts?: pulumi.Input<inputs.NexusEndpointTimeouts>;
    /**
     * A target spec for routing nexus requests to a specific cloud namespace worker.
     */
    workerTarget: pulumi.Input<inputs.NexusEndpointWorkerTarget>;
}