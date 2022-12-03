import { join } from "node:path";
import { readFile } from "node:fs/promises";

const filePath = new URL(join(import.meta.url, "..", "..", "input.txt"));

const file = await readFile(filePath, { encoding: "utf-8" });
const data = file.split("\n");

let score = 0;

for (let i = 0; i < data.length; i += 3) {
  const elf1 = data[i];
  const elf2 = data[i + 1];
  const elf3 = data[i + 2];

  for (const char of elf1) {
    if (elf2.includes(char) && elf3.includes(char)) {
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

