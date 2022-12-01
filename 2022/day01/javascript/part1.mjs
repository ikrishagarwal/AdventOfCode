import { join } from "node:path";
import { readFile } from "node:fs/promises";

const filePath = new URL(join(import.meta.url, "..", "..", "input.txt"));

const file = await readFile(filePath, { encoding: "utf-8" });
const data = file.split("\n");

const cal = [];
let current = 0;

for (let line of data) {
  if (line !== "") {
    current += parseInt(line);
  } else {
    cal.push(current);
    current = 0;
  }
}

console.log(Math.max(...cal));
