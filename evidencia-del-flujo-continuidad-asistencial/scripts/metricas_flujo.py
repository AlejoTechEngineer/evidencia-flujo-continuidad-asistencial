"""
Calcula la metrica en pareja del tablero: percentiles de tiempo de ciclo (flujo)
y envejecimiento de items (control), a partir de la exportacion del tablero.

Uso:
    python scripts/metricas_flujo.py data/tablero_export.csv
"""
import sys
import pandas as pd


def cargar(ruta: str) -> pd.DataFrame:
    df = pd.read_csv(ruta, parse_dates=["fecha_entrada", "fecha_salida"])
    return df


def percentiles(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby("tipo")["tiempo_ciclo_dias"]
    tabla = pd.DataFrame({
        "n": g.size(),
        "P50": g.quantile(0.50).round(1),
        "P85": g.quantile(0.85).round(1),
    })
    tabla["P85/P50"] = (tabla["P85"] / tabla["P50"]).round(2)
    return tabla.sort_values("P85", ascending=False)


def resumen(df: pd.DataFrame) -> dict:
    return {
        "items": len(df),
        "no_planeado_pct": round((df["planeado"] == "No").mean() * 100, 1),
        "expedites": int((df["expedite"] == "Si").sum()),
        "P50_global": float(df["tiempo_ciclo_dias"].quantile(0.50)),
        "P85_global": float(df["tiempo_ciclo_dias"].quantile(0.85)),
        "items_bloqueados": int((df["bloqueado_dias"] > 0).sum()),
    }


def main() -> None:
    ruta = sys.argv[1] if len(sys.argv) > 1 else "data/tablero_export.csv"
    df = cargar(ruta)

    r = resumen(df)
    print("=" * 62)
    print("INDICADORES DEL CRITERIO DOMINANTE")
    print("=" * 62)
    print(f"Items en ventana                 : {r['items']}")
    print(f"Trabajo no planeado              : {r['no_planeado_pct']} %")
    print(f"Tiempo de ciclo P50 / P85        : {r['P50_global']:.0f} / {r['P85_global']:.0f} dias")
    print(f"Cociente P85/P50 (variabilidad)  : {r['P85_global'] / r['P50_global']:.1f}")
    print(f"Expedites registrados            : {r['expedites']}")
    print(f"Items con bloqueo                : {r['items_bloqueados']}")
    print()
    print("PERCENTILES POR TIPO DE ITEM")
    print("-" * 62)
    print(percentiles(df).to_string())
    print()
    print("Lectura: comprometer por P85 y no por promedio. Si el P85 baja pero")
    print("el cumplimiento de WIP cae por debajo de 80 %, la mejora no es sostenible.")


if __name__ == "__main__":
    main()
