// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Fetches details about all Service Accounts.
 */
export function getServiceAccounts(opts?: pulumi.InvokeOptions): Promise<GetServiceAccountsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("temporalcloud:index/getServiceAccounts:getServiceAccounts", {
    }, opts);
}

/**
 * A collection of values returned by getServiceAccounts.
 */
export interface GetServiceAccountsResult {
    /**
     * The unique identifier of the Service Accounts data source.
     */
    readonly id: string;
    /**
     * The list of Service Accounts.
     */
    readonly serviceAccounts: outputs.GetServiceAccountsServiceAccount[];
}
/**
 * Fetches details about all Service Accounts.
 */
export function getServiceAccountsOutput(opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetServiceAccountsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("temporalcloud:index/getServiceAccounts:getServiceAccounts", {
    }, opts);
}
