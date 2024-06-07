CREATE TABLE notification_emails(
	id SERIAL PRIMARY KEY,
	recipient_id INT,
	subject VARCHAR(100),
	body VARCHAR(255)
);

CREATE OR REPLACE FUNCTION
	trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER AS
$$
	BEGIN
		INSERT INTO
			notification_emails(recipient_id, subject, body)
		VALUES
			(
				NEW.id,
				CONCAT_WS(' ', 'Balance change for account:', NEW.id),
				CONCAT_WS(' ', 'On', DATE(NOW()), 'your balance was changed from',
							OLD.balance, 'to', NEW.balance, '.')
			);
		RETURN NEW;
	END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER
	tr_send_email_on_balance_change
AFTER UPDATE ON
	logs
FOR EACH ROW
EXECUTE FUNCTION
	trigger_fn_send_email_on_balance_change();
