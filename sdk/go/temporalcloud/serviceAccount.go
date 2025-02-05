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

// Provisions a Temporal Cloud Service Account.
//
// ## Import
//
// Service Accounts can be imported to incorporate existing Service Accounts into your Terraform pipeline.
//
// # To import a Service Account, you need
//
// - a resource configuration in your Terraform configuration file/module to accept the imported Service Account. In the example below, the placeholder is "temporalcloud_service_account" "saimport"
//
// - the Service Accounts's ID, which is found using the Temporal Cloud CLI tcld sa l. In the example below, this is e3cb94fbdbb845f480044d053d00665b
//
// ```sh
// $ pulumi import temporalcloud:index/serviceAccount:ServiceAccount saimport e3cb94fbdbb845f480044d053d00665b
// ```
type ServiceAccount struct {
	pulumi.CustomResourceState

	// The role on the account. Must be one of admin, developer, or read (case-insensitive).
	AccountAccess pulumi.StringOutput `pulumi:"accountAccess"`
	// The name associated with the service account.
	Name pulumi.StringOutput `pulumi:"name"`
	// The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
	NamespaceAccesses ServiceAccountNamespaceAccessArrayOutput `pulumi:"namespaceAccesses"`
	// The current state of the Service Account.
	State    pulumi.StringOutput             `pulumi:"state"`
	Timeouts ServiceAccountTimeoutsPtrOutput `pulumi:"timeouts"`
}

// NewServiceAccount registers a new resource with the given unique name, arguments, and options.
func NewServiceAccount(ctx *pulumi.Context,
	name string, args *ServiceAccountArgs, opts ...pulumi.ResourceOption) (*ServiceAccount, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AccountAccess == nil {
		return nil, errors.New("invalid value for required argument 'AccountAccess'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ServiceAccount
	err := ctx.RegisterResource("temporalcloud:index/serviceAccount:ServiceAccount", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServiceAccount gets an existing ServiceAccount resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServiceAccount(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceAccountState, opts ...pulumi.ResourceOption) (*ServiceAccount, error) {
	var resource ServiceAccount
	err := ctx.ReadResource("temporalcloud:index/serviceAccount:ServiceAccount", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServiceAccount resources.
type serviceAccountState struct {
	// The role on the account. Must be one of admin, developer, or read (case-insensitive).
	AccountAccess *string `pulumi:"accountAccess"`
	// The name associated with the service account.
	Name *string `pulumi:"name"`
	// The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
	NamespaceAccesses []ServiceAccountNamespaceAccess `pulumi:"namespaceAccesses"`
	// The current state of the Service Account.
	State    *string                 `pulumi:"state"`
	Timeouts *ServiceAccountTimeouts `pulumi:"timeouts"`
}

type ServiceAccountState struct {
	// The role on the account. Must be one of admin, developer, or read (case-insensitive).
	AccountAccess pulumi.StringPtrInput
	// The name associated with the service account.
	Name pulumi.StringPtrInput
	// The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
	NamespaceAccesses ServiceAccountNamespaceAccessArrayInput
	// The current state of the Service Account.
	State    pulumi.StringPtrInput
	Timeouts ServiceAccountTimeoutsPtrInput
}

func (ServiceAccountState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceAccountState)(nil)).Elem()
}

type serviceAccountArgs struct {
	// The role on the account. Must be one of admin, developer, or read (case-insensitive).
	AccountAccess string `pulumi:"accountAccess"`
	// The name associated with the service account.
	Name *string `pulumi:"name"`
	// The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
	NamespaceAccesses []ServiceAccountNamespaceAccess `pulumi:"namespaceAccesses"`
	Timeouts          *ServiceAccountTimeouts         `pulumi:"timeouts"`
}

// The set of arguments for constructing a ServiceAccount resource.
type ServiceAccountArgs struct {
	// The role on the account. Must be one of admin, developer, or read (case-insensitive).
	AccountAccess pulumi.StringInput
	// The name associated with the service account.
	Name pulumi.StringPtrInput
	// The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
	NamespaceAccesses ServiceAccountNamespaceAccessArrayInput
	Timeouts          ServiceAccountTimeoutsPtrInput
}

func (ServiceAccountArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceAccountArgs)(nil)).Elem()
}

type ServiceAccountInput interface {
	pulumi.Input

	ToServiceAccountOutput() ServiceAccountOutput
	ToServiceAccountOutputWithContext(ctx context.Context) ServiceAccountOutput
}

func (*ServiceAccount) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceAccount)(nil)).Elem()
}

func (i *ServiceAccount) ToServiceAccountOutput() ServiceAccountOutput {
	return i.ToServiceAccountOutputWithContext(context.Background())
}

func (i *ServiceAccount) ToServiceAccountOutputWithContext(ctx context.Context) ServiceAccountOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceAccountOutput)
}

// ServiceAccountArrayInput is an input type that accepts ServiceAccountArray and ServiceAccountArrayOutput values.
// You can construct a concrete instance of `ServiceAccountArrayInput` via:
//
//	ServiceAccountArray{ ServiceAccountArgs{...} }
type ServiceAccountArrayInput interface {
	pulumi.Input

	ToServiceAccountArrayOutput() ServiceAccountArrayOutput
	ToServiceAccountArrayOutputWithContext(context.Context) ServiceAccountArrayOutput
}

type ServiceAccountArray []ServiceAccountInput

func (ServiceAccountArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServiceAccount)(nil)).Elem()
}

func (i ServiceAccountArray) ToServiceAccountArrayOutput() ServiceAccountArrayOutput {
	return i.ToServiceAccountArrayOutputWithContext(context.Background())
}

func (i ServiceAccountArray) ToServiceAccountArrayOutputWithContext(ctx context.Context) ServiceAccountArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceAccountArrayOutput)
}

// ServiceAccountMapInput is an input type that accepts ServiceAccountMap and ServiceAccountMapOutput values.
// You can construct a concrete instance of `ServiceAccountMapInput` via:
//
//	ServiceAccountMap{ "key": ServiceAccountArgs{...} }
type ServiceAccountMapInput interface {
	pulumi.Input

	ToServiceAccountMapOutput() ServiceAccountMapOutput
	ToServiceAccountMapOutputWithContext(context.Context) ServiceAccountMapOutput
}

type ServiceAccountMap map[string]ServiceAccountInput

func (ServiceAccountMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServiceAccount)(nil)).Elem()
}

func (i ServiceAccountMap) ToServiceAccountMapOutput() ServiceAccountMapOutput {
	return i.ToServiceAccountMapOutputWithContext(context.Background())
}

func (i ServiceAccountMap) ToServiceAccountMapOutputWithContext(ctx context.Context) ServiceAccountMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceAccountMapOutput)
}

type ServiceAccountOutput struct{ *pulumi.OutputState }

func (ServiceAccountOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceAccount)(nil)).Elem()
}

func (o ServiceAccountOutput) ToServiceAccountOutput() ServiceAccountOutput {
	return o
}

func (o ServiceAccountOutput) ToServiceAccountOutputWithContext(ctx context.Context) ServiceAccountOutput {
	return o
}

// The role on the account. Must be one of admin, developer, or read (case-insensitive).
func (o ServiceAccountOutput) AccountAccess() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceAccount) pulumi.StringOutput { return v.AccountAccess }).(pulumi.StringOutput)
}

// The name associated with the service account.
func (o ServiceAccountOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceAccount) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
func (o ServiceAccountOutput) NamespaceAccesses() ServiceAccountNamespaceAccessArrayOutput {
	return o.ApplyT(func(v *ServiceAccount) ServiceAccountNamespaceAccessArrayOutput { return v.NamespaceAccesses }).(ServiceAccountNamespaceAccessArrayOutput)
}

// The current state of the Service Account.
func (o ServiceAccountOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceAccount) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

func (o ServiceAccountOutput) Timeouts() ServiceAccountTimeoutsPtrOutput {
	return o.ApplyT(func(v *ServiceAccount) ServiceAccountTimeoutsPtrOutput { return v.Timeouts }).(ServiceAccountTimeoutsPtrOutput)
}

type ServiceAccountArrayOutput struct{ *pulumi.OutputState }

func (ServiceAccountArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServiceAccount)(nil)).Elem()
}

func (o ServiceAccountArrayOutput) ToServiceAccountArrayOutput() ServiceAccountArrayOutput {
	return o
}

func (o ServiceAccountArrayOutput) ToServiceAccountArrayOutputWithContext(ctx context.Context) ServiceAccountArrayOutput {
	return o
}

func (o ServiceAccountArrayOutput) Index(i pulumi.IntInput) ServiceAccountOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ServiceAccount {
		return vs[0].([]*ServiceAccount)[vs[1].(int)]
	}).(ServiceAccountOutput)
}

type ServiceAccountMapOutput struct{ *pulumi.OutputState }

func (ServiceAccountMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServiceAccount)(nil)).Elem()
}

func (o ServiceAccountMapOutput) ToServiceAccountMapOutput() ServiceAccountMapOutput {
	return o
}

func (o ServiceAccountMapOutput) ToServiceAccountMapOutputWithContext(ctx context.Context) ServiceAccountMapOutput {
	return o
}

func (o ServiceAccountMapOutput) MapIndex(k pulumi.StringInput) ServiceAccountOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ServiceAccount {
		return vs[0].(map[string]*ServiceAccount)[vs[1].(string)]
	}).(ServiceAccountOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceAccountInput)(nil)).Elem(), &ServiceAccount{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceAccountArrayInput)(nil)).Elem(), ServiceAccountArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceAccountMapInput)(nil)).Elem(), ServiceAccountMap{})
	pulumi.RegisterOutputType(ServiceAccountOutput{})
	pulumi.RegisterOutputType(ServiceAccountArrayOutput{})
	pulumi.RegisterOutputType(ServiceAccountMapOutput{})
}
