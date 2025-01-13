// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Pulumi.Xyz
{
    public static class Config
    {
        [global::System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("xyz");

        private static readonly __Value<Pulumi.Xyz.Region.Region?> _region = new __Value<Pulumi.Xyz.Region.Region?>(() => __config.GetObject<Pulumi.Xyz.Region.Region>("region"));
        /// <summary>
        /// A region which should be used.
        /// </summary>
        public static Pulumi.Xyz.Region.Region? Region
        {
            get => _region.Get();
            set => _region.Set(value);
        }

    }
}
