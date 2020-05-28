# Example of instantiating a wasm module and calling an export on it

from pathlib import Path

from wasmtime import Store, Module, Instance

examples = Path(__file__).resolve().parent


def main():
    store = Store()
    module = Module.from_file(store, examples / "gcd.wat")
    instance = Instance(module, [])
    gcd = instance.exports["gcd"]

    print("gcd(6, 27) = %d" % gcd(6, 27))


if __name__ == "__main__":
    main()
