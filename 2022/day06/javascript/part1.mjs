import { join } from "node:path";
import { readFile } from "node:fs/promises";

const filePath = new URL(join(import.meta.url, "..", "..", "input.txt"));

const file = await readFile(filePath, { encoding: "utf-8" });
const data = file.split("\n")[0];

const memory = [];
let i = 0;
for (; i < data.length; i++) {
  const letter = data[i];
  memory.splice(0, memory.indexOf(letter) + 1);
  memory.push(letter);

  if (memory.length === 4) break;
}

console.log(i + 1);
