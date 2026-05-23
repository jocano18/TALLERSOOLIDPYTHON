"""Verificación de los paquetes *_SOL sin modificar los originales."""

from dip.dip_SOL import BackEnd, FrontEnd
from isp.isp_SOL import IPrintable, ModernPrinter, OldPrinter
from lsp.lsp_SOL import Rectangle, Square, total_area
from ocp.ocp_SOL import AreaCalculator, Circle, Rectangle as OcpRectangle
from srp.srp_SOL import FileManager, FileReader, FileWriter


def verify_dip() -> None:
    FrontEnd(BackEnd()).display_data()


def verify_isp() -> None:
    def imprimir(printer: IPrintable, doc: str) -> None:
        printer.print(doc)

    imprimir(OldPrinter(), "doc.pdf")
    imprimir(ModernPrinter(), "doc.pdf")


def verify_lsp() -> None:
    assert total_area([Rectangle(4, 5), Square(3)]) == 29.0


def verify_ocp() -> None:
    total = AreaCalculator.total_area([OcpRectangle(4, 5), Circle(2)])
    assert abs(total - (20 + 3.141592653589793 * 4)) < 1e-9


def verify_srp(tmp_path) -> None:
    path = tmp_path / "nota.txt"
    fm = FileManager(path)
    fm.write("hola")
    assert fm.read() == "hola"

    writer = FileWriter(path)
    reader = FileReader(path)
    writer.write("mundo")
    assert reader.read() == "mundo"


if __name__ == "__main__":
    verify_dip()
    verify_isp()
    verify_lsp()
    verify_ocp()
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp:
        verify_srp(Path(tmp))
    print("Todos los paquetes *_SOL verificados correctamente.")
