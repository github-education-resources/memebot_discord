import fs from "fs";

export default function loadFiles(dirName, ext) {
  const files = fs.readdirSync(dirName);
  const filteredFiles = files.filter((file) => file.endsWith(ext));
  return filteredFiles;
}
