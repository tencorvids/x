{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python312
    python312Packages.gitpython
    python312Packages.click
  ];

  shellHook = ''
    export POETRY_VIRTUALENVS_IN_PROJECT=true
    export POETRY_VIRTUALENVS_CREATE=true
    echo "Python and Poetry environment loaded"
    echo "Python version: $(python --version)"
    echo "Poetry version: $(poetry --version)"

    if [ -d .venv ]; then
        source .venv/bin/activate
    fi
  '';
}
