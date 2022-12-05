import { join } from "node:path";
import { readFile } from "node:fs/promises";

const filePath = new URL(join(import.meta.url, "..", "..", "input.txt"));

const file = await readFile(filePath, { encoding: "utf-8" });
const data = file.split("\n");
const stack = {};

let j = 0;

for (let [i, line] of data.entries()) {
  if (!isNaN(Number(String(line).trim()[0]))) {
    j = i + 2;
    break;
  }

  for (let j = 1; j < line.length; j += 4) {
    let k = (j % 4) + Math.floor(j / 4);
    if (String(line[j]).trim().length !== 0) {
      stack[k] = stack[k] ? stack[k] : [];
      stack[k].unshift(line[j]);
    }
  }
}

for (; j < data.length; j++) {
  const line = data[j];
  const count = isNaN(Number(line[5]))
    ? Number(line[5])
    : Number(line[5] + line[6]);

  const giver = Number(line[count > 9 ? 13 : 12]);
  const receiver = Number(line[line.length - 1]);

  const move = stack[giver].splice(stack[giver].length - count);
  stack[receiver].push(...move);
}

console.log(
  Object.values(stack)
    .map((item) => item[item.length - 1])
    .join("")
);
