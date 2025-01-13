package shim

import (
	"github.com/hashicorp/terraform-plugin-framework/provider"
	temporalcloud "github.com/temporalio/terraform-provider-temporalcloud/internal/provider"
)

func New(version string) func() provider.Provider {
	return temporalcloud.New(version)
}
