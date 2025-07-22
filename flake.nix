{
  description = "Dev environment for mtlynch.io";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";

    # 18.14.1 release
    nodejs-nixpkgs.url = "github:NixOS/nixpkgs/6adf48f53d819a7b6e15672817fa1e78e5f4e84f";

    # 0.147.5 release
    hugo-nixpkgs.url = "github:NixOS/nixpkgs/e0042dedfbc9134ef973f64e5c7f56a38cc5cc97";

    # 0.17.0 release
    htmltest-nixpkgs.url = "github:NixOS/nixpkgs/076e8c6678d8c54204abcb4b1b14c366835a58bb";
  };

  outputs = {
    self,
    flake-utils,
    nodejs-nixpkgs,
    hugo-nixpkgs,
    htmltest-nixpkgs,
  } @ inputs:
    flake-utils.lib.eachDefaultSystem (system: let
      hugo = hugo-nixpkgs.legacyPackages.${system}.hugo;
      nodejs = nodejs-nixpkgs.legacyPackages.${system}.nodejs-18_x;
      htmltest = htmltest-nixpkgs.legacyPackages.${system}.htmltest;
      libxml2 = hugo-nixpkgs.legacyPackages.${system}.libxml2;
      imagemagick = hugo-nixpkgs.legacyPackages.${system}.imagemagick;
      jq = hugo-nixpkgs.legacyPackages.${system}.jq;
      wget = hugo-nixpkgs.legacyPackages.${system}.wget;
      exiftool = hugo-nixpkgs.legacyPackages.${system}.exiftool;
    in {
      devShells.default = hugo-nixpkgs.legacyPackages.${system}.mkShell {
        packages = [
          hugo
          htmltest
          libxml2
          nodejs
          imagemagick
          jq
          wget
          exiftool
        ];

        shellHook = ''
          magick --version | head -n 1 | sed 's/Version: //' | awk '{print $1, $2, $3, $4, $5}'
          echo "exiftool" "$(exiftool -ver)"
          jq --version
          htmltest --version
          echo "node" "$(node --version)"
          hugo version
        '';
      };

      formatter = hugo-nixpkgs.legacyPackages.${system}.alejandra;
    });
}
