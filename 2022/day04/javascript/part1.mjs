import { join } from "node:path";
import { readFile } from "node:fs/promises";

const filePath = new URL(join(import.meta.url, "..", "..", "input.txt"));

const file = await readFile(filePath, { encoding: "utf-8" });
const data = file.split("\n");

let overlap = 0;

for (const line in data) {
  const elf1 = data[line]
    .split(",")[0]
    .split("-")
    .map((n) => Number(n));

  const elf2 = data[line]
    .split(",")[1]
    .split("-")
    .map((n) => Number(n));

  if (elf1[0] <= elf2[0] && elf1[1] >= elf2[1]) {
    overlap++;
  } else if (elf2[0] <= elf1[0] && elf2[1] >= elf1[1]) {
    overlap++;
  }
}

console.log(overlap);
