degree=1
for state_var in conservative primitive; do
    for nx in 8 4 2 1; do
        mpiexec.hydra -n 6 build/fluids-navierstokes -options_file examples/fluids/blasius.yaml -ts_adapt_monitor -state_var $state_var -degree $degree -dm_plex_box_faces $((40/$nx)),$((64/$nx)),1 -platemesh_Ndelta $((45/$nx)) -platemesh_growth $(bc -l <<<"1.08 ^ $nx") -ts_dt $(bc -l <<<"0.0000001 * $nx * $degree") -log_view >examples/fluids/results/blasius/${state_var}_p${degree}_res${nx}.log
    done
done