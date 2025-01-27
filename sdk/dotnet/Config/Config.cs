// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Pulumi.Temporalcloud
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

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("temporalcloud");

        private static readonly __Value<bool?> _allowInsecure = new __Value<bool?>(() => __config.GetBoolean("allowInsecure"));
        /// <summary>
        /// If set to True, it allows for an insecure connection to the Temporal Cloud API. This should never be set to 'true' in
        /// production and defaults to false.
        /// </summary>
        public static bool? AllowInsecure
        {
            get => _allowInsecure.Get();
            set => _allowInsecure.Set(value);
        }

        private static readonly __Value<string?> _allowedAccountId = new __Value<string?>(() => __config.Get("allowedAccountId"));
        /// <summary>
        /// The ID of the account to operate on. Prevents accidental mutation of accounts other than that provided.
        /// </summary>
        public static string? AllowedAccountId
        {
            get => _allowedAccountId.Get();
            set => _allowedAccountId.Set(value);
        }

        private static readonly __Value<string?> _apiKey = new __Value<string?>(() => __config.Get("apiKey"));
        /// <summary>
        /// The API key for Temporal Cloud. See [this documentation](https://docs.temporal.io/cloud/api-keys) for information on how
        /// to obtain an API key.
        /// </summary>
        public static string? ApiKey
        {
            get => _apiKey.Get();
            set => _apiKey.Set(value);
        }

        private static readonly __Value<string?> _endpoint = new __Value<string?>(() => __config.Get("endpoint"));
        /// <summary>
        /// The endpoint for the Temporal Cloud API. Defaults to `saas-api.tmprl.cloud:443`.
        /// </summary>
        public static string? Endpoint
        {
            get => _endpoint.Get();
            set => _endpoint.Set(value);
        }

    }
}
