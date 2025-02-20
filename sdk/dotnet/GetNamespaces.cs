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
    public static class GetNamespaces
    {
        /// <summary>
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Temporalcloud = Pulumi.Temporalcloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var myNamespaces = Temporalcloud.GetNamespaces.Invoke();
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["namespaces"] = myNamespaces.Apply(getNamespacesResult =&gt; getNamespacesResult.Namespaces),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Task<GetNamespacesResult> InvokeAsync(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNamespacesResult>("temporalcloud:index/getNamespaces:getNamespaces", InvokeArgs.Empty, options.WithDefaults());

        /// <summary>
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Temporalcloud = Pulumi.Temporalcloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var myNamespaces = Temporalcloud.GetNamespaces.Invoke();
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["namespaces"] = myNamespaces.Apply(getNamespacesResult =&gt; getNamespacesResult.Namespaces),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetNamespacesResult> Invoke(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNamespacesResult>("temporalcloud:index/getNamespaces:getNamespaces", InvokeArgs.Empty, options.WithDefaults());

        /// <summary>
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Temporalcloud = Pulumi.Temporalcloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var myNamespaces = Temporalcloud.GetNamespaces.Invoke();
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["namespaces"] = myNamespaces.Apply(getNamespacesResult =&gt; getNamespacesResult.Namespaces),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetNamespacesResult> Invoke(InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetNamespacesResult>("temporalcloud:index/getNamespaces:getNamespaces", InvokeArgs.Empty, options.WithDefaults());
    }


    [OutputType]
    public sealed class GetNamespacesResult
    {
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.GetNamespacesNamespaceResult> Namespaces;

        [OutputConstructor]
        private GetNamespacesResult(
            string id,

            ImmutableArray<Outputs.GetNamespacesNamespaceResult> namespaces)
        {
            Id = id;
            Namespaces = namespaces;
        }
    }
}
