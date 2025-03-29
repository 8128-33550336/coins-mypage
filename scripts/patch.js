const fs = require("fs");

const pkgFile = fs.readFileSync("./package.json", "utf8");
const pkg = JSON.parse(pkgFile);

const patch = (version) => {
  const parts = version.split(".");
  if (parts.length !== 3) {
    throw new Error("Invalid version format");
  }
  parts[2] = parseInt(parts[2]) + 1;
  return parts.join(".");
};

const newVersion = patch(pkg.version);
const newPkg = { ...pkg, version: newVersion };
const newPkgFile = JSON.stringify(newPkg, null, 2);

fs.writeFileSync("./package.json", newPkgFile, "utf8");
console.error(`Version updated from ${pkg.version} to ${newVersion}`);

const newVersionTag = `v${newVersion}`;
console.log(`::set-output name=tag::${newVersionTag}`);
