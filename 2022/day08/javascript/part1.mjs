import { join } from "node:path";
import { readFile } from "node:fs/promises";

const filePath = new URL(join(import.meta.url, "..", "..", "input.txt"));

const file = await readFile(filePath, { encoding: "utf-8" });
const data = file.split("\n");

let visible = data[0].length * 2 + data.length * 2 - 4;
const treeMap = data.map((row) => row.split("").map(Number));

for (let i = 1; i < data.length - 1; i++) {
  for (let j = 1; j < data[i].length - 1; j++) {
    const tree = treeMap[i][j];
    const leftRow = [...treeMap[i]].splice(0, j);
    const rightRow = [...treeMap[i]].splice(j + 1, data[i].length);

    if (Math.max(...leftRow) < tree || Math.max(...rightRow) < tree)
      visible += 1;
    else {
      const topList = [];
      const bottomList = [];

      for (let k = 0; k < i; k++) {
        topList.push(treeMap[k][j]);
      }

      for (let k = i + 1; k < treeMap.length; k++) {
        bottomList.push(treeMap[k][j]);
      }

      if (Math.max(...topList) < tree || Math.max(...bottomList) < tree)
        visible += 1;
    }
  }
}

console.log(visible);
