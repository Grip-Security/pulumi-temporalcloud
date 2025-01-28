// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { ApikeyArgs, ApikeyState } from "./apikey";
export type Apikey = import("./apikey").Apikey;
export const Apikey: typeof import("./apikey").Apikey = null as any;
utilities.lazyLoad(exports, ["Apikey"], () => require("./apikey"));

export { GetNamespacesResult } from "./getNamespaces";
export const getNamespaces: typeof import("./getNamespaces").getNamespaces = null as any;
export const getNamespacesOutput: typeof import("./getNamespaces").getNamespacesOutput = null as any;
utilities.lazyLoad(exports, ["getNamespaces","getNamespacesOutput"], () => require("./getNamespaces"));

export { GetRegionsResult } from "./getRegions";
export const getRegions: typeof import("./getRegions").getRegions = null as any;
export const getRegionsOutput: typeof import("./getRegions").getRegionsOutput = null as any;
utilities.lazyLoad(exports, ["getRegions","getRegionsOutput"], () => require("./getRegions"));

export { GetServiceAccountsResult } from "./getServiceAccounts";
export const getServiceAccounts: typeof import("./getServiceAccounts").getServiceAccounts = null as any;
export const getServiceAccountsOutput: typeof import("./getServiceAccounts").getServiceAccountsOutput = null as any;
utilities.lazyLoad(exports, ["getServiceAccounts","getServiceAccountsOutput"], () => require("./getServiceAccounts"));

export { MetricsEndpointArgs, MetricsEndpointState } from "./metricsEndpoint";
export type MetricsEndpoint = import("./metricsEndpoint").MetricsEndpoint;
export const MetricsEndpoint: typeof import("./metricsEndpoint").MetricsEndpoint = null as any;
utilities.lazyLoad(exports, ["MetricsEndpoint"], () => require("./metricsEndpoint"));

export { NamespaceArgs, NamespaceState } from "./namespace";
export type Namespace = import("./namespace").Namespace;
export const Namespace: typeof import("./namespace").Namespace = null as any;
utilities.lazyLoad(exports, ["Namespace"], () => require("./namespace"));

export { NamespaceSearchAttributeArgs, NamespaceSearchAttributeState } from "./namespaceSearchAttribute";
export type NamespaceSearchAttribute = import("./namespaceSearchAttribute").NamespaceSearchAttribute;
export const NamespaceSearchAttribute: typeof import("./namespaceSearchAttribute").NamespaceSearchAttribute = null as any;
utilities.lazyLoad(exports, ["NamespaceSearchAttribute"], () => require("./namespaceSearchAttribute"));

export { NexusEndpointArgs, NexusEndpointState } from "./nexusEndpoint";
export type NexusEndpoint = import("./nexusEndpoint").NexusEndpoint;
export const NexusEndpoint: typeof import("./nexusEndpoint").NexusEndpoint = null as any;
utilities.lazyLoad(exports, ["NexusEndpoint"], () => require("./nexusEndpoint"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { ServiceAccountArgs, ServiceAccountState } from "./serviceAccount";
export type ServiceAccount = import("./serviceAccount").ServiceAccount;
export const ServiceAccount: typeof import("./serviceAccount").ServiceAccount = null as any;
utilities.lazyLoad(exports, ["ServiceAccount"], () => require("./serviceAccount"));

export { UserArgs, UserState } from "./user";
export type User = import("./user").User;
export const User: typeof import("./user").User = null as any;
utilities.lazyLoad(exports, ["User"], () => require("./user"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "temporalcloud:index/apikey:Apikey":
                return new Apikey(name, <any>undefined, { urn })
            case "temporalcloud:index/metricsEndpoint:MetricsEndpoint":
                return new MetricsEndpoint(name, <any>undefined, { urn })
            case "temporalcloud:index/namespace:Namespace":
                return new Namespace(name, <any>undefined, { urn })
            case "temporalcloud:index/namespaceSearchAttribute:NamespaceSearchAttribute":
                return new NamespaceSearchAttribute(name, <any>undefined, { urn })
            case "temporalcloud:index/nexusEndpoint:NexusEndpoint":
                return new NexusEndpoint(name, <any>undefined, { urn })
            case "temporalcloud:index/serviceAccount:ServiceAccount":
                return new ServiceAccount(name, <any>undefined, { urn })
            case "temporalcloud:index/user:User":
                return new User(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("temporalcloud", "index/apikey", _module)
pulumi.runtime.registerResourceModule("temporalcloud", "index/metricsEndpoint", _module)
pulumi.runtime.registerResourceModule("temporalcloud", "index/namespace", _module)
pulumi.runtime.registerResourceModule("temporalcloud", "index/namespaceSearchAttribute", _module)
pulumi.runtime.registerResourceModule("temporalcloud", "index/nexusEndpoint", _module)
pulumi.runtime.registerResourceModule("temporalcloud", "index/serviceAccount", _module)
pulumi.runtime.registerResourceModule("temporalcloud", "index/user", _module)
pulumi.runtime.registerResourcePackage("temporalcloud", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:temporalcloud") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});