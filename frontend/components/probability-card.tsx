type ProbabilityCardProps = {
  name: string;
  value: number;
  tone?: "teal" | "amber" | "rose";
};

const toneClass = {
  teal: "text-teal",
  amber: "text-amber",
  rose: "text-rose",
};

export function ProbabilityCard({ name, value, tone = "teal" }: ProbabilityCardProps) {
  return (
    <article className="min-h-28 rounded-lg border border-line bg-panel p-4">
      <p className="text-xs uppercase text-muted">{name}</p>
      <strong className={`mt-3 block text-3xl ${toneClass[tone]}`}>{Math.round(value)}%</strong>
    </article>
  );
}
