
from schulplots.converter import converter
from schulplots.figure_description import FigureDescription

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        prog="schulplots.py", 
        description="Create function plots styled similar to the conventions used in German schools."
    )
    parser.add_argument("filename", help="Description of the figure, in YAML format")
    parser.add_argument("--output", "-o", help="name out output file. If not provided, an interactive window is shown.")

    args = parser.parse_args()
    fdsc = converter.loads(open(args.filename, "r").read(), FigureDescription)
    if args.output is not None:
        fdsc.figure.output_file = args.output
    fdsc.create_figure()
        
