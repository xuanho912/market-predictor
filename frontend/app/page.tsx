import { MarketDashboard } from "../components/market-dashboard";
import { getPredictionDashboard } from "../lib/api";

export const dynamic = "force-static";

export default async function Home() {
  const dashboard = await getPredictionDashboard();
  return <MarketDashboard dashboard={dashboard} />;
}
