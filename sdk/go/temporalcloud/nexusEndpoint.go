// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package temporalcloud

import (
	"context"
	"reflect"

	"errors"
	"github.com/Grip-Security/pulumi-temporalcloud/sdk/go/temporalcloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provisions a Temporal Cloud Nexus endpoint.
//
// ## Import
//
// Nexus Endpoints can be imported to incorporate existing Nexus Endpoints into your Terraform pipeline.
//
// # To import a Nexus Endpoint, you need
//
// - a resource configuration in your Terraform configuration file/module to accept the imported Nexus Endpoint. In the example below, the placeholder is "temporalcloud_nexus_endpoint" "nexus_endpoint"
//
// - the Nexus Endpoint's ID, which is found using the Temporal Cloud CLI tcld nexus endpoint list. In the example below, this is 405f7da4224a43d99c211904ed9b3819
//
// ```sh
// $ pulumi import temporalcloud:index/nexusEndpoint:NexusEndpoint nexus_endpoint 405f7da4224a43d99c211904ed9b3819
// ```
type NexusEndpoint struct {
	pulumi.CustomResourceState

	// Namespace Id(s) that are allowed to call this Endpoint.
	AllowedCallerNamespaces pulumi.StringArrayOutput `pulumi:"allowedCallerNamespaces"`
	// The description for the Nexus endpoint.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The name of the endpoint. Must be unique within an account and match `^[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9]$`
	Name     pulumi.StringOutput            `pulumi:"name"`
	Timeouts NexusEndpointTimeoutsPtrOutput `pulumi:"timeouts"`
	// A target spec for routing nexus requests to a specific cloud namespace worker.
	WorkerTarget NexusEndpointWorkerTargetOutput `pulumi:"workerTarget"`
}

// NewNexusEndpoint registers a new resource with the given unique name, arguments, and options.
func NewNexusEndpoint(ctx *pulumi.Context,
	name string, args *NexusEndpointArgs, opts ...pulumi.ResourceOption) (*NexusEndpoint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AllowedCallerNamespaces == nil {
		return nil, errors.New("invalid value for required argument 'AllowedCallerNamespaces'")
	}
	if args.WorkerTarget == nil {
		return nil, errors.New("invalid value for required argument 'WorkerTarget'")
	}
	if args.Description != nil {
		args.Description = pulumi.ToSecret(args.Description).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"description",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource NexusEndpoint
	err := ctx.RegisterResource("temporalcloud:index/nexusEndpoint:NexusEndpoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNexusEndpoint gets an existing NexusEndpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNexusEndpoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NexusEndpointState, opts ...pulumi.ResourceOption) (*NexusEndpoint, error) {
	var resource NexusEndpoint
	err := ctx.ReadResource("temporalcloud:index/nexusEndpoint:NexusEndpoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NexusEndpoint resources.
type nexusEndpointState struct {
	// Namespace Id(s) that are allowed to call this Endpoint.
	AllowedCallerNamespaces []string `pulumi:"allowedCallerNamespaces"`
	// The description for the Nexus endpoint.
	Description *string `pulumi:"description"`
	// The name of the endpoint. Must be unique within an account and match `^[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9]$`
	Name     *string                `pulumi:"name"`
	Timeouts *NexusEndpointTimeouts `pulumi:"timeouts"`
	// A target spec for routing nexus requests to a specific cloud namespace worker.
	WorkerTarget *NexusEndpointWorkerTarget `pulumi:"workerTarget"`
}

type NexusEndpointState struct {
	// Namespace Id(s) that are allowed to call this Endpoint.
	AllowedCallerNamespaces pulumi.StringArrayInput
	// The description for the Nexus endpoint.
	Description pulumi.StringPtrInput
	// The name of the endpoint. Must be unique within an account and match `^[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9]$`
	Name     pulumi.StringPtrInput
	Timeouts NexusEndpointTimeoutsPtrInput
	// A target spec for routing nexus requests to a specific cloud namespace worker.
	WorkerTarget NexusEndpointWorkerTargetPtrInput
}

func (NexusEndpointState) ElementType() reflect.Type {
	return reflect.TypeOf((*nexusEndpointState)(nil)).Elem()
}

type nexusEndpointArgs struct {
	// Namespace Id(s) that are allowed to call this Endpoint.
	AllowedCallerNamespaces []string `pulumi:"allowedCallerNamespaces"`
	// The description for the Nexus endpoint.
	Description *string `pulumi:"description"`
	// The name of the endpoint. Must be unique within an account and match `^[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9]$`
	Name     *string                `pulumi:"name"`
	Timeouts *NexusEndpointTimeouts `pulumi:"timeouts"`
	// A target spec for routing nexus requests to a specific cloud namespace worker.
	WorkerTarget NexusEndpointWorkerTarget `pulumi:"workerTarget"`
}

// The set of arguments for constructing a NexusEndpoint resource.
type NexusEndpointArgs struct {
	// Namespace Id(s) that are allowed to call this Endpoint.
	AllowedCallerNamespaces pulumi.StringArrayInput
	// The description for the Nexus endpoint.
	Description pulumi.StringPtrInput
	// The name of the endpoint. Must be unique within an account and match `^[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9]$`
	Name     pulumi.StringPtrInput
	Timeouts NexusEndpointTimeoutsPtrInput
	// A target spec for routing nexus requests to a specific cloud namespace worker.
	WorkerTarget NexusEndpointWorkerTargetInput
}

func (NexusEndpointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*nexusEndpointArgs)(nil)).Elem()
}

type NexusEndpointInput interface {
	pulumi.Input

	ToNexusEndpointOutput() NexusEndpointOutput
	ToNexusEndpointOutputWithContext(ctx context.Context) NexusEndpointOutput
}

func (*NexusEndpoint) ElementType() reflect.Type {
	return reflect.TypeOf((**NexusEndpoint)(nil)).Elem()
}

func (i *NexusEndpoint) ToNexusEndpointOutput() NexusEndpointOutput {
	return i.ToNexusEndpointOutputWithContext(context.Background())
}

func (i *NexusEndpoint) ToNexusEndpointOutputWithContext(ctx context.Context) NexusEndpointOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NexusEndpointOutput)
}

// NexusEndpointArrayInput is an input type that accepts NexusEndpointArray and NexusEndpointArrayOutput values.
// You can construct a concrete instance of `NexusEndpointArrayInput` via:
//
//	NexusEndpointArray{ NexusEndpointArgs{...} }
type NexusEndpointArrayInput interface {
	pulumi.Input

	ToNexusEndpointArrayOutput() NexusEndpointArrayOutput
	ToNexusEndpointArrayOutputWithContext(context.Context) NexusEndpointArrayOutput
}

type NexusEndpointArray []NexusEndpointInput

func (NexusEndpointArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NexusEndpoint)(nil)).Elem()
}

func (i NexusEndpointArray) ToNexusEndpointArrayOutput() NexusEndpointArrayOutput {
	return i.ToNexusEndpointArrayOutputWithContext(context.Background())
}

func (i NexusEndpointArray) ToNexusEndpointArrayOutputWithContext(ctx context.Context) NexusEndpointArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NexusEndpointArrayOutput)
}

// NexusEndpointMapInput is an input type that accepts NexusEndpointMap and NexusEndpointMapOutput values.
// You can construct a concrete instance of `NexusEndpointMapInput` via:
//
//	NexusEndpointMap{ "key": NexusEndpointArgs{...} }
type NexusEndpointMapInput interface {
	pulumi.Input

	ToNexusEndpointMapOutput() NexusEndpointMapOutput
	ToNexusEndpointMapOutputWithContext(context.Context) NexusEndpointMapOutput
}

type NexusEndpointMap map[string]NexusEndpointInput

func (NexusEndpointMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NexusEndpoint)(nil)).Elem()
}

func (i NexusEndpointMap) ToNexusEndpointMapOutput() NexusEndpointMapOutput {
	return i.ToNexusEndpointMapOutputWithContext(context.Background())
}

func (i NexusEndpointMap) ToNexusEndpointMapOutputWithContext(ctx context.Context) NexusEndpointMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NexusEndpointMapOutput)
}

type NexusEndpointOutput struct{ *pulumi.OutputState }

func (NexusEndpointOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NexusEndpoint)(nil)).Elem()
}

func (o NexusEndpointOutput) ToNexusEndpointOutput() NexusEndpointOutput {
	return o
}

func (o NexusEndpointOutput) ToNexusEndpointOutputWithContext(ctx context.Context) NexusEndpointOutput {
	return o
}

// Namespace Id(s) that are allowed to call this Endpoint.
func (o NexusEndpointOutput) AllowedCallerNamespaces() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *NexusEndpoint) pulumi.StringArrayOutput { return v.AllowedCallerNamespaces }).(pulumi.StringArrayOutput)
}

// The description for the Nexus endpoint.
func (o NexusEndpointOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NexusEndpoint) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The name of the endpoint. Must be unique within an account and match `^[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9]$`
func (o NexusEndpointOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *NexusEndpoint) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o NexusEndpointOutput) Timeouts() NexusEndpointTimeoutsPtrOutput {
	return o.ApplyT(func(v *NexusEndpoint) NexusEndpointTimeoutsPtrOutput { return v.Timeouts }).(NexusEndpointTimeoutsPtrOutput)
}

// A target spec for routing nexus requests to a specific cloud namespace worker.
func (o NexusEndpointOutput) WorkerTarget() NexusEndpointWorkerTargetOutput {
	return o.ApplyT(func(v *NexusEndpoint) NexusEndpointWorkerTargetOutput { return v.WorkerTarget }).(NexusEndpointWorkerTargetOutput)
}

type NexusEndpointArrayOutput struct{ *pulumi.OutputState }

func (NexusEndpointArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NexusEndpoint)(nil)).Elem()
}

func (o NexusEndpointArrayOutput) ToNexusEndpointArrayOutput() NexusEndpointArrayOutput {
	return o
}

func (o NexusEndpointArrayOutput) ToNexusEndpointArrayOutputWithContext(ctx context.Context) NexusEndpointArrayOutput {
	return o
}

func (o NexusEndpointArrayOutput) Index(i pulumi.IntInput) NexusEndpointOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *NexusEndpoint {
		return vs[0].([]*NexusEndpoint)[vs[1].(int)]
	}).(NexusEndpointOutput)
}

type NexusEndpointMapOutput struct{ *pulumi.OutputState }

func (NexusEndpointMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NexusEndpoint)(nil)).Elem()
}

func (o NexusEndpointMapOutput) ToNexusEndpointMapOutput() NexusEndpointMapOutput {
	return o
}

func (o NexusEndpointMapOutput) ToNexusEndpointMapOutputWithContext(ctx context.Context) NexusEndpointMapOutput {
	return o
}

func (o NexusEndpointMapOutput) MapIndex(k pulumi.StringInput) NexusEndpointOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *NexusEndpoint {
		return vs[0].(map[string]*NexusEndpoint)[vs[1].(string)]
	}).(NexusEndpointOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NexusEndpointInput)(nil)).Elem(), &NexusEndpoint{})
	pulumi.RegisterInputType(reflect.TypeOf((*NexusEndpointArrayInput)(nil)).Elem(), NexusEndpointArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NexusEndpointMapInput)(nil)).Elem(), NexusEndpointMap{})
	pulumi.RegisterOutputType(NexusEndpointOutput{})
	pulumi.RegisterOutputType(NexusEndpointArrayOutput{})
	pulumi.RegisterOutputType(NexusEndpointMapOutput{})
}
