degree=2
for state_var in conservative primitive; do
    for nx in 8 4 2; do
        mpiexec.hydra -n 6 build/fluids-navierstokes -options_file examples/fluids/blasiusP2.yaml -ts_adapt_monitor -state_var $state_var -degree $degree -dm_plex_box_faces $((20/$nx)),$((32/$nx)),1 -platemesh_Ndelta $((22/$nx)) -platemesh_growth $(bc -l <<<"1.1664 ^ $nx") -ts_dt $(bc -l <<<"0.0000001 * $nx * $degree") -log_view >examples/fluids/results/blasius/${state_var}_p${degree}_res${nx}.log
    done
done
