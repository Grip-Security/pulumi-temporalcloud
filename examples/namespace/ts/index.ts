import * as temporalcloud from "@pulumi/temporalcloud";

const namespace = new temporalcloud.Namespace("namespace", {
  name: "pulumi-test",
  regions: ["aws-us-east-2"],
  retentionDays: 14,
  apiKeyAuth: true,
});

export const namespaceId = namespace.id;
