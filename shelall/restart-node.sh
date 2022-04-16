pkill massa-node
screen -XS mas_auto quit
screen -dmS mas_auto
screen -S mas_auto -X stuff "cd ~/massa/massa-node/ && RUST_BACKTRACE=full cargo run --release |& tee ~/nodeman-massa/logs/massa-hidden.logs"$(echo -ne '\015')
