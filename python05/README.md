# Python Module 05

Data processing architecture exercises focused on abstract base classes, protocols, adapters, and pipeline orchestration.

## Exercises

| # | Directory | File | Topic |
|---|-----------|------|-------|
| 0 | `ex0/` | `stream_processor.py` | ABC foundation with polymorphic processors (`NumericProcessor`, `TextProcessor`, `LogProcessor`) |
| 1 | `ex1/` | `data_stream.py` | Polymorphic stream system (`SensorStream`, `TransactionStream`, `EventStream`) and batch execution |
| 2 | `ex2/` | `nexus_pipeline.py` | Enterprise-style pipeline adapters (`JSONAdapter`, `CSVAdapter`, `StreamAdapter`) with staged processing and recovery |

## Concepts Practiced

- Abstract classes with `abc.ABC` and `@abstractmethod`
- Interface contracts using `typing.Protocol`
- Composition of processing stages
- Polymorphism across stream and adapter types
- Runtime stats collection and basic error recovery

## How To Run

From repository root:

```bash
python3 python05/ex0/stream_processor.py
python3 python05/ex1/data_stream.py
python3 python05/ex2/nexus_pipeline.py
```

From inside `python05/`:

```bash
python3 ex0/stream_processor.py
python3 ex1/data_stream.py
python3 ex2/nexus_pipeline.py
```

## Notes

- These scripts are self-contained demos with sample data in each `__main__` block.
- `ex2` intentionally demonstrates both normal flow and failure-handling behavior.
- No external packages are required beyond the Python standard library.
