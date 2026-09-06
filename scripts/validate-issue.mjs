#!/usr/bin/env node
import { readFile } from "node:fs/promises";

const FRAMES = ["Gate","Margin","Snapshot","Geometry","Distill","Appliance","Residency","Registry"];
const CARD_PRICES = ["$4k–$18k/mo","$199–$799/mo","$8k–$25k","$1.5k/unit · $8k/set","$15k + $3k/mo","$6k + $400/mo","€8k–€40k","$29 / $499 + 20% take"];
const KILL_RE = /\b(rumor|allegedly|sources say|leak|unconfirmed|procurement)\b/i;
const ISSUE_01_THESIS = "do not sell another chatbot wrapper. intelligence is cheap at the flash / spark tier. skills, gates, and local or sovereign runtime are not.";

const file = process.argv[2] ?? "issues/staging.json";
const raw = JSON.parse(await readFile(file, "utf8"));
const meta = raw.meta ?? raw.issue;
const items = raw.items;
const errors = [];

if (!meta?.id || !meta.title) errors.push("meta.id and meta.title required");
if (!Array.isArray(items) || items.length < 5 || items.length > 8) {
  errors.push(`items must be 5–8, got ${items?.length ?? 0}`);
}
if (meta?.id !== "01" && String(meta?.thesis ?? "").trim().toLowerCase() === ISSUE_01_THESIS) {
  errors.push("thesis is Issue 01 verbatim");
}

for (const [i, item] of (items ?? []).entries()) {
  if (!FRAMES.includes(item.frame)) errors.push(`items[${i}].frame invalid`);
  if (!CARD_PRICES.includes(item.sell?.price)) {
    errors.push(`items[${i}].sell.price not on card: ${item.sell?.price}`);
  }
  if (!item.sell?.product || !item.sell?.why) errors.push(`items[${i}].sell incomplete`);
  if (!item.stats?.length) errors.push(`items[${i}].stats missing`);
  const blob = `${item.title} ${item.lede} ${(item.body ?? []).join(" ")}`;
  if (KILL_RE.test(blob)) errors.push(`items[${i}] kill-list token`);
}

if (errors.length) {
  console.error("BLOCKED");
  for (const err of errors) console.error("-", err);
  process.exit(1);
}
console.log("GREEN", meta.id, meta.title, items.length, "items");
