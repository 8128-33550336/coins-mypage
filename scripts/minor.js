const fs = require("fs");

const pkgFile = fs.readFileSync("./package.json", "utf8");
const pkg = JSON.parse(pkgFile);

const minor = (version) => {
  const parts = version.split(".");
  if (parts.length !== 3) {
    throw new Error("Invalid version format");
  }
  parts[1] = parseInt(parts[1]) + 1;
  parts[2] = 0;
  return parts.join(".");
};

const newVersion = minor(pkg.version);
const newPkg = { ...pkg, version: newVersion };
const newPkgFile = JSON.stringify(newPkg, null, 2);

fs.writeFileSync("./package.json", newPkgFile, "utf8");
console.error(`Version updated from ${pkg.version} to ${newVersion}`);

const newVersionTag = `v${newVersion}`;
console.log(`tag=${newVersionTag}`);
