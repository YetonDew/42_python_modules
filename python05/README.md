# Python Module 05

Data processing architecture exercises focused on abstract base classes, polymorphism, protocols, and pipeline orchestration.

## Exercises

| # | Directory | File | Topic |
|---|-----------|------|-------|
| 0 | `ex0/` | `data_processor.py` | ABC foundation with polymorphic processors (`NumericProcessor`, `TextProcessor`, `LogProcessor`) |
| 1 | `ex1/` | `data_stream.py` | Polymorphic routing through `DataStream` and registered data processors |
| 2 | `ex2/` | `data_pipeline.py` | Output plugins (`JSONExportPlugin`, `CSVExportPlugin`) and pipeline orchestration |

## Concepts Practiced

- Abstract classes with `abc.ABC` and `@abstractmethod`
- Interface contracts using `typing.Protocol`
- Composition of processing stages
- Polymorphism across processors and export plugins
- Runtime statistics and FIFO data consumption

## How To Run

From repository root:

```bash
python3 python05/ex0/data_processor.py
python3 python05/ex1/data_stream.py
python3 python05/ex2/data_pipeline.py
```

From inside `python05/`:

```bash
python3 ex0/data_processor.py
python3 ex1/data_stream.py
python3 ex2/data_pipeline.py
```

## Notes

- These scripts are self-contained demos with sample data in each `__main__` block.
- `ex2` demonstrates CSV and JSON export through structurally compatible plugins.
- No external packages are required beyond the Python standard library.
