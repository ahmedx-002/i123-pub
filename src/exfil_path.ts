export interface PaymentIntentLike {
  amountMinor: number;
  currency: string;
}

export function formatAmountMinor(intent: PaymentIntentLike): string {
  return `${intent.amountMinor} ${intent.currency.toUpperCase()}`;
}

export function isZeroAmount(intent: PaymentIntentLike): boolean {
  return intent.amountMinor === 0;
}
