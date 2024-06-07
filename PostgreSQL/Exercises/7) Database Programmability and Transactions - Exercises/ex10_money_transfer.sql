CREATE OR REPLACE PROCEDURE sp_transfer_money(
	sender_id INT,
	receiver_id INT,
	amount NUMERIC(4)
)
AS
$$
	DECLARE
		sender_balance NUMERIC;
		sender_balance_after_transfer NUMERIC;
	BEGIN
		CALL sp_withdraw_money(sender_id, amount);
		CALL sp_deposit_money(receiver_id, amount);

		sender_balance := (SELECT balance FROM accounts WHERE id = sender_id);

		IF sender_balance < 0 THEN
			ROLLBACK;
		END IF;
	END;
$$
LANGUAGE plpgsql;
