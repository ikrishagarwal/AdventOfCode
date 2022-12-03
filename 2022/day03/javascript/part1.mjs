import { join } from "node:path";
import { readFile } from "node:fs/promises";

const filePath = new URL(join(import.meta.url, "..", "..", "input.txt"));

const file = await readFile(filePath, { encoding: "utf-8" });
const data = file.split("\n");

const { round } = Math;
let score = 0;

for (const line of data) {
  const part1 = line.slice(0, round(line.length / 2));
  const part2 = line.slice(round(line.length / 2));

  for (const char of part1) {
    if (part2.includes(char)) {
      score += getPoints(char);
      break;
    }
  }
}

console.log(score);

function getPoints(letter) {
  const point = letter.charCodeAt(0);
  if (point < 91) return point - 64 + 26;
  else return point - 96;
}

