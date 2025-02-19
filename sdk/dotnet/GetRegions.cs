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
    public static class GetRegions
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
        ///     var regions = Temporalcloud.GetRegions.Invoke();
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["regions"] = regions.Apply(getRegionsResult =&gt; getRegionsResult.Regions),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Task<GetRegionsResult> InvokeAsync(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetRegionsResult>("temporalcloud:index/getRegions:getRegions", InvokeArgs.Empty, options.WithDefaults());

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
        ///     var regions = Temporalcloud.GetRegions.Invoke();
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["regions"] = regions.Apply(getRegionsResult =&gt; getRegionsResult.Regions),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetRegionsResult> Invoke(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetRegionsResult>("temporalcloud:index/getRegions:getRegions", InvokeArgs.Empty, options.WithDefaults());

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
        ///     var regions = Temporalcloud.GetRegions.Invoke();
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["regions"] = regions.Apply(getRegionsResult =&gt; getRegionsResult.Regions),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetRegionsResult> Invoke(InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetRegionsResult>("temporalcloud:index/getRegions:getRegions", InvokeArgs.Empty, options.WithDefaults());
    }


    [OutputType]
    public sealed class GetRegionsResult
    {
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.GetRegionsRegionResult> Regions;

        [OutputConstructor]
        private GetRegionsResult(
            string id,

            ImmutableArray<Outputs.GetRegionsRegionResult> regions)
        {
            Id = id;
            Regions = regions;
        }
    }
}
