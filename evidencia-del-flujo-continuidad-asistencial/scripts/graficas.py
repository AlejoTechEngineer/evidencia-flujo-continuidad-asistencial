"""Genera el histograma y el scatter de tiempo de ciclo usados como evidencia minima."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/tablero_export.csv", parse_dates=["fecha_entrada", "fecha_salida"])
p50 = df.tiempo_ciclo_dias.quantile(0.50)
p85 = df.tiempo_ciclo_dias.quantile(0.85)

# --- Histograma ---
fig, ax = plt.subplots(figsize=(9, 4.6))
ax.hist(df.tiempo_ciclo_dias, bins=range(0, int(df.tiempo_ciclo_dias.max()) + 4, 3),
        color="#2E75B6", edgecolor="white")
ax.axvline(p50, color="#1E7145", linestyle="--", linewidth=2, label=f"P50 = {p50:.0f} dias")
ax.axvline(p85, color="#C00000", linestyle="--", linewidth=2, label=f"P85 = {p85:.0f} dias")
ax.set_title("Distribucion del tiempo de ciclo (8 semanas)", fontsize=12, weight="bold")
ax.set_xlabel("Tiempo de ciclo (dias)")
ax.set_ylabel("Numero de items")
ax.legend()
ax.grid(axis="y", alpha=0.25)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figuras/histograma_tiempo_ciclo.png", dpi=150)

# --- Scatter ---
colores = {"Evolutivo": "#2E75B6", "Incidente": "#1E7145",
           "Interoperabilidad": "#C00000", "Cumplimiento": "#ED7D31"}
fig, ax = plt.subplots(figsize=(9, 4.6))
for t, g in df.groupby("tipo"):
    ax.scatter(g.fecha_salida, g.tiempo_ciclo_dias, label=t, alpha=0.75,
               color=colores[t], edgecolor="white", s=45)
ax.axhline(p85, color="#C00000", linestyle="--", linewidth=1.6, label=f"P85 = {p85:.0f} dias")
ax.set_title("Dispersion del tiempo de ciclo por tipo de item", fontsize=12, weight="bold")
ax.set_xlabel("Fecha de salida")
ax.set_ylabel("Tiempo de ciclo (dias)")
ax.legend(fontsize=8, ncol=2)
ax.grid(alpha=0.25)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig("figuras/scatter_tiempo_ciclo.png", dpi=150)
print("figuras generadas")
