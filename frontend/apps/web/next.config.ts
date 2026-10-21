import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  transpilePackages: ["@vct/api-client", "@vct/contracts"],
  outputFileTracingIncludes: {
    "/api/v1/extension-download": ["./private/vct-connect-extension.zip"],
  },
};

export default nextConfig;
