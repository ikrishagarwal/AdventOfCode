import { join } from "node:path";
import { readFile } from "node:fs/promises";

const filePath = new URL(join(import.meta.url, "..", "..", "input.txt"));

const file = await readFile(filePath, { encoding: "utf-8" });
const data = file.split("\n");

const treeMap = data.map((row) => row.split("").map(Number));
const scoreList = [];

for (let i = 1; i < data.length - 1; i++) {
  for (let j = 1; j < data[i].length - 1; j++) {
    const tree = treeMap[i][j];

    const scores = [0, 0, 0, 0];

    for (let k = i - 1; k > -1; k--) {
      scores[0] += 1;
      if (treeMap[k][j] >= tree) break;
    }

    for (let k = i + 1; k < treeMap.length; k++) {
      scores[1] += 1;
      if (treeMap[k][j] >= tree) break;
    }

    for (const k of [...treeMap[i]].splice(0, j).reverse()) {
      scores[2] += 1;
      if (k >= tree) break;
    }

    for (const k of [...treeMap[i]].splice(j + 1, treeMap[i].length)) {
      scores[3] += 1;
      if (k >= tree) break;
    }

    scoreList.push(scores.reduce((a, i) => a * i, 1));
  }
}

console.log(Math.max(...scoreList));
